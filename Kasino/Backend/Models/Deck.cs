namespace Kasino.Models
{
  public class Deck
  {
    public List<Card>? Cards { get; set; }

    private readonly List<Suits> suit = Enum.GetValues(typeof(Suits)).Cast<Suits>().ToList();
    private readonly List<int> value = Enumerable.Range(1, 10).ToList(); // Values 1 to 10

    public Deck()
    {
      InitializeDeck();
    }

    private void InitializeDeck()
    {
      int id = 1;
      Cards = suit.SelectMany(suit => value, (suit, value) => new Card(id++, suit, value)).ToList();
      Shuffle();
    }

    public void Shuffle()
    {
      var rng = new Random();
      if (Cards != null)
      {
        Cards = Cards.OrderBy(c => rng.Next()).ToList();
      }
    }

    public Card? DishCard()
    {
      // Ensure Cards is not null and has elements before proceeding
      if (Cards == null || Cards.Count == 0)
      {
        return null; // No cards left to deal, safely return null with nullable return type
      }

      // Directly access the first card using indexing
      var card = Cards[0];
      Cards.RemoveAt(0);
      return card;
    }
  }
}