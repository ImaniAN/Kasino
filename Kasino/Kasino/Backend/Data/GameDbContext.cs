using Kasino.Models;
using System.Data.Entity;

namespace Kasino.Data
{
  /// <summary>
  /// Represents the database context for the game application
  /// </summary>
  public class GameDbContext : DbContext
  {
    /// <summary>
    /// Constructor for GameDbContext that initializes with the provided options
    /// </summary>
    /// <param name="options">The options for configuring the context</param>
    public GameDbContext(DbContextOptions<GameDbContext> options) : base(options) { }

    /// <summary>
    /// Gets or sets the DbSet of Cards
    /// </summary>
    public DbSet<Card> Cards { get; set; }

    /// <summary>
    /// Gets or sets the DbSet of Decks
    /// </summary>
    public DbSet<Deck> Decks { get; set; }

    /// <summary>
    /// Gets or sets the DbSet of Games
    /// </summary>
    public DbSet<Game> Games { get; set; }

    /// <summary>
    /// Gets or sets the DbSet of Players
    /// </summary>
    public DbSet<Player> Players { get; set; }

    /// <summary>
    /// Gets or sets the DbSet of Moves
    /// </summary>
    public DbSet<Move> Moves { get; set; }

    /// <summary>
    /// Gets the entry for a player
    /// </summary>
    /// <param name="player">The player object</param>
    /// <returns>The entry for the player</returns>
    internal object Entry(Player player)
    {
      throw new NotImplementedException();
    }

    /// <summary>
    /// Save changes to the context
    /// </summary>
    internal void SaveChanges()
    {
      throw new NotImplementedException();
    }

    /// <summary>
    /// Asynchronously save changes to the context
    /// </summary>
    internal async Task SaveChangesAsync()
    {
      throw new NotImplementedException();
    }
  }

  public class DbContextOptions<T>
  {
  }
}