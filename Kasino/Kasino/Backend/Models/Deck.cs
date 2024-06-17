namespace Kasino.Models
{  /*This code defines a Deck class with methods to shuffle the cards in the deck and draw a card from the deck. 
    * The Shuffle method randomizes the order of cards in the deck, and the DrawCard method removes and returns 
    * the top card from the deck.*/

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