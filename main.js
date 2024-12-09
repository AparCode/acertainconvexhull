let points = []; // Array to store user input points
let hull = []; // Array to store points forming the convex hull
let isPaused = false; // Pause state
let isRunning = false; // Whether Jarvis March is running
let endHull = false;
let currentStep = 0; // Current step in the algorithm
let leftmost; // Leftmost point
let p, q; // Current and next points in the hull, respectively
let checkIndex = 0; // Index of the point being checked
let speed = 10; // Speed of execution (lower = slower)
let currentLine = ""; // Current pseudocode line being executed
let delay = 500; // Default delay between steps in milliseconds

// Helper variable to control execution timing
let lastExecutionTime = 0;

let draggedPointIndex = null; // Index of the dragged point
let width = 800;
let height = 600;

function setup() {
    const canvas = createCanvas(width, height);
    canvas.parent('canvas-container');
    resetCanvas(false); // Clear the canvas and display instructions
}

function draw() {
    translate(width / 2, height / 2); // Set the origin (0,0) to the center of the canvas
    resetCanvas(false); // Clear the canvas and display instructions

    highlightPseudocode();

    // Draw all points
    for (let i = 0; i < points.length; i++) {
        fill(0);
        noStroke();
        ellipse(points[i].x, points[i].y, 8, 8);
    }

    // Draw the convex hull
    if (hull.length > 1) {
        stroke(0);
        strokeWeight(2);
        noFill();
        beginShape();
        for (let i = 0; i < hull.length; i++) {
            vertex(hull[i].x, hull[i].y);
        }

        if(endHull){
        vertex(hull[0].x, hull[0].y); // Close the hull
        endShape();
        }
        else{
            endShape();
        }
    }

    // Execute Jarvis March steps with variable speed
    if (isRunning && !isPaused) {
        delay = map(speed, 1, 20, 1000, 50);
        if (millis() - lastExecutionTime > delay) {
            stepJarvisMarch();
            lastExecutionTime = millis();
        }
    }

    // Update the dragged point's position
    if (draggedPointIndex !== null) {
        canDrag = 1;
        points[draggedPointIndex].x = mouseX - width / 2;
        points[draggedPointIndex].y = mouseY - height / 2;
        newp = draggedPointIndex;

        // check if the point is past an edge already created (WIP)
        // for (let p = 0; p < hull.length; p++){
        //     for (let q = 0; q < hull.length; q++){
        //         if (hull[p] != points[draggedPointIndex] && hull[q] != points[draggedPointIndex] && p != q){
        //             if (ccw(points[p], points[draggedPointIndex], points[q]) < 0){
        //                 canDrag = -1;
        //             }
        //         }
        //     }
        // }
        // console.log(canDrag);
        // if (canDrag <= 1){
        //     points[draggedPointIndex].x = mouseX - width / 2;
        //     points[draggedPointIndex].y = mouseY - height / 2;
        //     newp = draggedPointIndex;
        // }
    } else {
        newp = p;
    }

    // Draw the current test line
    if (isRunning && currentStep === 1 && checkIndex < points.length) {
        stroke(255, 0, 0, 100); // Transparent red for test lines
        strokeWeight(1);
        line(points[p].x, points[p].y, points[checkIndex].x, points[checkIndex].y);
    }
}

function mousePressed() {
    const x = mouseX - width / 2;
    const y = mouseY - height / 2;

    if ((!isRunning || isPaused) && mouseX >= 0 && mouseX <= width && mouseY >= 0 && mouseY <= height) {

        // Check if the click is on any point
        for (let i = 0; i < points.length; i++) {
            const d = dist(x, y, points[i].x, points[i].y);
            if (d < 8) { // If click is near the point (within 8 pixels)
                draggedPointIndex = i; // Set this point to be dragged
                return;
            }
        }

        if (draggedPointIndex !== null) {
            return;
        }

        // If no point is clicked, add a new point
        points.push(createVector(x, y));
    }
}

function mouseReleased() {
    draggedPointIndex = null; // Stop dragging
}

// Highlight pseudocode line
function highlightPseudocode() {
    const pseudocodeLines = ["line1", "line2", "line2a", "line2a1", "line2b", "line2c"];

    // Remove highlight from all lines and highlight only the current line
    for (const line of pseudocodeLines) {
        document.getElementById(line).classList.remove("highlight");
    }
    if (currentLine) {
        document.getElementById(currentLine).classList.add("highlight");
    }
}

// Execute the start of the Jarvis March algorithm
function startJarvisMarch() {
    if (points.length < 3) {
        alert('At least 3 points are needed to compute a convex hull.');
        return;
    }
    if (isRunning) return;

    isRunning = true;
    isPaused = false;
    hull = [];
    currentStep = 0;

    // Initialize p as the leftmost point
    leftmost = 0;
    for (let i = 1; i < points.length; i++) {
        if (points[i].x < points[leftmost].x) {
            leftmost = i;
        } else if (points[i].x === points[leftmost].x) {
            // if two points have the same x-coordinate, choose the one with the lower y-coordinate
            if (points[i].y < points[leftmost].y) {
                leftmost = i;
            }
        }
        p = leftmost;
        currentLine = "line1"; // Highlight step 1
    }
}

// Execute a single step of the Jarvis March algorithm based on the current step
function stepJarvisMarch() {

    // If current step is 0, add the leftmost point to the hull and update q
    if (currentStep === 0) {
        currentLine = "line1"; // Highlight initializing p for the pseudocode
        hull.push(points[p]);
        q = (p + 1) % points.length; // Set q to the next point in the hull, wrap if needed
        checkIndex = 0; // Reset the check index to the first point
        currentStep = 1;

    // If current step is 1, check all points to find the next point in the hull
    } else if (currentStep === 1) {
        currentLine = "line2a1"; // Highlight searching for q, for the pseudocode

        if (checkIndex < points.length) {
            // If the point we're checking (c) is on the right side of the line from p to q, update q to c
            if (ccw(points[p], points[checkIndex], points[q]) > 0) {
                q = checkIndex;
            }
            checkIndex++;

        } else {

            currentLine = "line2b"; // Highlight storing q for the pseudocode
            highlightPseudocode(); // Highlight the next line since this is an intermediate step

            // Set p to q and then add q to the hull on the next iteration
            p = q;

            // If we've returned to the leftmost point, stop the algorithm
            if (p === leftmost) {
                isRunning = false;
                endHull = true;
                currentLine = ""; // Clear the highlight

            // Otherwise, move to the next point in the hull
            } else {
                currentLine = "line2c"; // Highlight setting p = q for the pseudocode
            }
            currentStep = 0; // Move to the next point in the hull
        }
    }
}

function ccw(p, q, r) {
    // Calculate cross product to determine if the points are to the left of the line or not
    return (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
}

// Transform points using the 3x3 matrix
function transformPoints() {
    const a = parseFloat(document.getElementById('matrix-a').value);
    const b = parseFloat(document.getElementById('matrix-b').value);
    const c = parseFloat(document.getElementById('matrix-c').value);
    const d = parseFloat(document.getElementById('matrix-d').value);
    const tx = parseFloat(document.getElementById('matrix-tx').value);
    const ty = parseFloat(document.getElementById('matrix-ty').value);

    // Apply the transformation matrix to each point
    points = points.map(pt => {
        const newX = a * pt.x + b * pt.y + tx;
        const newY = c * pt.x + d * pt.y + ty;
        return createVector(newX, newY);
    });

    // Start the Jarvis March algorithm with the transformed points
    resetAlgorithm();
}

// Pause the algorithm
function pause() {
    isPaused = true;
}

// Resume the algorithm
function resume() {
    isPaused = false;
}

// Reset the algorithm but keep the points
function resetAlgorithm() {
    hull = [];
    isPaused = false;
    isRunning = false;
    currentStep = 0;
    checkIndex = 0;
    lastExecutionTime = 0;
    currentLine = ""; // Reset pseudocode highlight
    resetCanvas(true);
    if (points.length > 0) {
        startJarvisMarch();
    }
}

// Reset everything including the points
function resetProgram() {
    points = [];
    resetAlgorithm();
}

// Update speed value based on slider input
function updateSpeed() {
    speed = parseInt(document.getElementById('speedSlider').value);
    document.getElementById('speedValue').innerText = speed;
}

// Clear the canvas and display instructions
function resetCanvas() {
    background(240); // Clear the canvas
    fill(0);
    textSize(16);
    // if (!fromAlgorithm) {
    //     text('Click anywhere to add points. Use the buttons to interact.', -width / 2 + 10, -height / 2 + 20);
    // }
}