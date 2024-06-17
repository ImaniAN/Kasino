using Kasino.Models;


/// <summary>
/// Represents a build in the game, consisting of a collection of cards and the player who owns the build.
/// </summary>
public class Build
{
  /// <summary>
  /// Gets or sets the owner of the build.
  /// </summary>
  public Player Owner { get; set; }

  /// <summary>
  /// Gets or sets the list of cards that make up the build.
  /// </summary>
  public List<Card> Cards { get; set; } = new List<Card>();

  /// <summary>
  /// Initializes a new instance of the <see cref="Build"/> class with a specified owner and list of cards.
  /// </summary>
  /// <param name="owner">The player who owns the build.</param>
  /// <param name="cards">The list of cards that make up the build.</param>
  public Build(Player owner, List<Card> cards)
  {
    Owner = owner;
    Cards = cards;
  }
}
