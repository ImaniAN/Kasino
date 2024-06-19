using Kasino.Backend.Models;

namespace Kasino.Models
{
  /*This code defines a Game class that represents a card game. It has properties for 
   * Id, Players, FloorCards, Deck, and CurrentRound. 
   * It also includes methods for dealing cards, capturing cards, building, Lahlaring, and calculating scores in the game.*/
  public class Game
  {
    public string? Id { get; set; }
    public List<Player> Players { get; set; } = new List<Player>();
    public List<Card> FloorCards { get; set; } = new List<Card>();
    public Deck Deck { get; set; } = new Deck();
    public int CurrentRound { get; set; }

    public List<Build> Builds { get; set; } = new List<Build>();

    // Method to add a Build object to the game state
    public void AddBuildToGameState(Build build)
    {
      // Add the build to the Builds collection
      Builds.Add(build);

      // Additional logic to handle the build in the game state
      // For example, you might need to notify players, update the game board, etc.
    }

    // Method to check if a card is special based on more complex criteria
    public static bool IsCardSpecial(Card card)
    {
      // Example logic: A card is special if it's an Ace or Jack
      return card.Value == 1 || card.Value == 11;
    }

    public void DealCards()
    {
      int cardsPerPlayer;

      switch (Players.Count)
      {
        case 2 or 4:
          cardsPerPlayer = 10;
          break;
        case 3:
          cardsPerPlayer = 13; // 13 cards per player
          break;
        default:
          throw new InvalidOperationException("Unsupported number of players");
      }

      // Deal cards to players
      foreach (var player in Players)
      {
        for (int i = 0; i < cardsPerPlayer; i++)
        {
          var card = Deck.DishCard();
          if (card != null)
          {
            player.Hand.Add(card);
          }
        }
      }
    }


    public void Capture(Card playedCard, Player player)
    {
      // List to hold cards to be captured from the floor
      List<Card> capturedCards = new List<Card>();

      // Check if the played card can directly capture any floor card
      foreach (var floorCard in FloorCards)
      {
        if (playedCard.Value == floorCard.Value)
        {
          capturedCards.Add(floorCard);
        }
      }

      // If direct capture is not possible, check for combinations that sum up to the played card's value
      // This part can get complex depending on the rules for combinations
      // For simplicity, this example does not include combination logic

      // Remove captured cards from the floor and add them to the player's CapturedCards
      foreach (var card in capturedCards)
      {
        FloorCards.Remove(card);
        player.CapturedCards.Add(card); // Assuming each player has a 'CapturedCards' to store captured cards
      }

      // Also add the played card to the player's CapturedCards
      player.CapturedCards.Add(playedCard);

      // Additional logic for special captures or scoring might go here
    }


    public void Build(Card playedCard, Player player, int targetValue)
    {
      // List to hold potential build cards from the floor
      List<Card> potentialBuildCards = new List<Card>();

      // Check if there are combinations on the floor that sum up to the target value
      foreach (var floorCard in FloorCards)
      {
        if (playedCard.Value + floorCard.Value == targetValue)
        {
          potentialBuildCards.Add(floorCard);
        }
      }

      // If a valid build is possible
      if (potentialBuildCards.Any())
      {
        // Correctly instantiate a Build object with the player and the combined cards
        Build newBuild = new Build(player, new List<Card> { playedCard }.Concat(potentialBuildCards).ToList());


        // Remove the played card from the player's hand
        player.Hand.Remove(playedCard);

        // Remove the used floor cards
        foreach (var card in potentialBuildCards)
        {
          FloorCards.Remove(card);
        }

        // Example solution for handling builds:
        // Assuming there's a method to add builds to the game state
        AddBuildToGameState(newBuild);

        // Note: You'll need to implement the AddBuildToGameState method or similar
        // to properly handle the new+-Build object according to your game's rules.
      }
      else
      {
        // Handle the case where a build is not possible
        throw new InvalidOperationException("Build is not possible with the provided card and target value.");
      }
    }


    public void Lahla(Card playedCard, Player player)
    {
      // Check if Lahlaring is allowed based on game rules
      // For example, in some in 2 player 1st round, Lahlaring might is not allowed if the player can capture
      // This example does not include such logic for simplicity

      // Remove the played card from the player's hand
      player.Hand.Remove(playedCard);

      // Add the played card to the floor
      FloorCards.Add(playedCard);

      // Additional logic for special Lahlaring rules or effects might go here
    }

    public void CalculateScores()
    {
      foreach (var player in Players)
      {
        int score = 0;
        List<Card> capturedCards = player.CapturedCards;

        // Basic scoring: 1 point per captured card
        score += capturedCards.Count;

        // Additional scoring based on specific rules
        int totalCards = capturedCards.Count;
        int spadesCount = capturedCards.Count(card => card.Suit == Suits.S);
        int diamondsCount = capturedCards.Count(card => card.Value == 10 && card.Suit == Suits.D);
        int spadesTwoCount = capturedCards.Count(card => card.Value == 2 && card.Suit == Suits.S);
        int acesCount = capturedCards.Count(card => card.Value == 1);

        score += totalCards / 20; // 1 point for every 20 cards
        score += totalCards > 20 ? 2 : 0; // 2 points for more than 20 cards
        score += spadesCount > 5 ? 1 : 0; // 1 point for more than 5 Spades
        score += diamondsCount == 1 ? 2 : 0; // 2 points for capturing Ten of Diamonds
        score += spadesTwoCount == 1 ? 1 : 0; // 1 point for capturing Two of Spades
        score += acesCount; // 1 point for each Ace captured

        // Update the player's score
        player.Score += score;
      }

      // Additional scoring logic and determining the round or game winner can be added here
    }

  }
}