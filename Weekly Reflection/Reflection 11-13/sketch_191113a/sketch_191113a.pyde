void setup() {
  size(800,600);
  line(0, 0, 800, 600);
  
  ellipse(790, 10, 20, 20);
  
  ellipse(10, 590, 20, 20);
  
  square(200, 10, 55);
  
  //returns an error saying the left hand side must be a variable, unable to resolve
  for(int circle = 0 ; circle <= 30 ; circle = circle + 1) {
     ellipse(790 – ((780/30) * circle), 10 + ((580/30) * circle), 20, 20);
   }

}
