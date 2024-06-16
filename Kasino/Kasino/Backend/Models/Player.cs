public class Player
{
  public string PlayerId { get; set; }
  public string Name { get; set; }
  public List<Card> Hand { get; set; } = new List<Card>();
  public List<Card> CapturedCards { get; set; } = new List<Card>();
  public int Score { get; set; }

  // Additional properties and methods relevant to the player
}
