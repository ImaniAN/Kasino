namespace Kasino.Models
{
  public class Move
  {
    public Player Player { get; set; }
    public Card PlayedCard { get; set; }
    public string ActionType { get; set; } // e.g., "Capture", "Build", "Trail"
  }
}
