public class Build
{
  public Player Owner { get; set; }
  public List<Card> Cards { get; set; } = new List<Card>();

  // Constructor for creating a new build
  public Build(Player owner, List<Card> cards)
  {
    Owner = owner;
    Cards = cards;
  }
}
