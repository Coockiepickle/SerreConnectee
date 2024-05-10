void setup() {
  // Initialisation du générateur de nombres aléatoires avec une graine
  randomSeed(analogRead(0));
}
 
void loop() {
 
  int AirAleatoire = random(101);
 
  // Affichage du nombre aléatoire sur le moniteur série
  Serial.print("L'humidité est de ");
  Serial.print(AirAleatoire);
  Serial.println(" %");
 
  // Attente de quelques secondes
  delay(1000);
}
