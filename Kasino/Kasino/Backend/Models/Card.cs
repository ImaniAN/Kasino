namespace Kasino.Models
{
  public enum Suits
  {
    S,
    H,
    C,
    D
  }

  public class Card
  {
    public int Id { get; set; }
    public Suits Suit { get; set; }
    public int Value { get; set; }

    // Add a new constructor that accepts id, suit, and value
    public Card(int id, Suits suit, int value)
    {
      Id = id;
      Suit = suit;
      Value = value;
    }

    public bool IsSpecialCard()
    {
      // Example logic for identifying a special card
      return (Suit == Suits.D && Value == 10) || (Suit == Suits.S && Value == 2) || Value == 1;
    }

    public int PointValue()
    {
      // Example logic for determining the point value of a card
      if (Suit == Suits.D && Value == 10) return 2;
      if (Suit == Suits.S && Value == 2) return 1;
      if (Value == 1) return 1; // Aces
      return 0;
    }
  }
}
