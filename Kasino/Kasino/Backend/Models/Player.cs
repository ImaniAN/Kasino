namespace Kasino.Models
{
  public class Player
  {
    public string Id { get; set; }
    public string Name { get; set; }
    public List<Card> Hand { get; set; } = new List<Card>();
    public List<Card> CapturedCards { get; set; } = new List<Card>();
    public int Score { get; set; }
  }
}
