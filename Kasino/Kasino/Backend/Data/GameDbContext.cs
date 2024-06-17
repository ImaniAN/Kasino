using Kasino.Models;

namespace Kasino.Data
{
  public class GameDbContext : DbContext
  {/*This code defines a GameDbContext class that inherits from DbContext and represents the database context. 
    * It includes properties to access specific database tables such as Cards, Decks, Games, Players, and Moves.*/
    public GameDbContext(DbContextOptions<GameDbContext> options) : base(options) { }

    public DbSet<Card> Cards { get; set; }
    public DbSet<Deck> Decks { get; set; }
    public DbSet<Game> Games { get; set; }
    public DbSet<Player> Players { get; set; }
    public DbSet<Move> Moves { get; set; }

  }
}
