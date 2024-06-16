namespace Kasino.Models
{
  public class Game
  {
    public string Id { get; set; }
    public List<Player> Players { get; set; } = new List<Player>();
    public List<Card> TableCards { get; set; } = new List<Card>();
    public Deck Deck { get; set; } = new Deck();
    public int CurrentRound { get; set; }

    public void DealCards()
    {
      foreach (var player in Players)
      {
        player.Hand.Add(Deck.DrawCard());
        player.Hand.Add(Deck.DrawCard());
      }

      for (int i = 0; i < 4; i++)
      {
        TableCards.Add(Deck.DrawCard());
      }
    }

    public void Capture(Card playedCard, Player player)
    {
      // Implement capture logic
    }

    public void Build(Card playedCard, Player player, int targetValue)
    {
      // Implement build logic
    }

    public void Trail(Card playedCard, Player player)
    {
      // Implement trailing logic
    }

    public void CalculateScores()
    {
      // Implement scoring logic
    }
  }
}