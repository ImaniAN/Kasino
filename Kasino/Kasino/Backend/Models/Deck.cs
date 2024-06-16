namespace Kasino.Models
{
  public class Deck
  {
    public List<Card> Cards { get; set; } = new List<Card>();

    public void Shuffle()
    {
      var rng = new Random();
      Cards = Cards.OrderBy(c => rng.Next()).ToList();
    }

    public Card DrawCard()
    {
      if (Cards.Count == 0)
        return null;

      var card = Cards[0];
      Cards.RemoveAt(0);
      return card;
    }
  }
}