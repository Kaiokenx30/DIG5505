float mean(float[] sequence) {
float sum = 0;
for (int i = 0; i < sequence.length; i++) {
sum = sum + sequence[i];
}
return sum/sequence.length;
}
float[] values = {10, 9, 73, 25, 33, 76, 52, 1, 35, 86};
void setup() {
  size(200,100);
  //rect(30,15,20,10);
  for (int i = 0; i < values.length; i++){
   rect(i * 20,100 - values[i],20,values[i]); 
  }
rect(0, 100 - mean(values), 200, 0);
println(mean(values));
}
