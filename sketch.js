function setup() {
  createCanvas(600, 600);
}

function draw() {
  background(0, 255, 255);
  // circle(50,50,25);
}

function mousePressed() {
  createPoint();
  console.log(mouseX)
}

function createPoint(){
  let x = mouseX;
  let y = mouseY;
  circle(x,y,20);
}