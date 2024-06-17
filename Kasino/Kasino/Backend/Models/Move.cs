namespace Kasino.Models
{
  public class Move
  {  /*This code defines a class named Move with properties for a Player, a PlayedCard, and an ActionType 
      * (e.g., "Capture", "Build", "Trail").*/
    public Player Player { get; set; }
    public Card PlayedCard { get; set; }
    public string ActionType { get; set; } // e.g., "Capture", "Build", "Trail"
  }
}