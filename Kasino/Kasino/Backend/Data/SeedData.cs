using Kasino.Data;
using Kasino.Models;

namespace YourNamespace
{
  public static class SeedData
  {/*This code defines a static class SeedData with a method Initialize that seeds the database with initial data 
    * for games and players if no games are found in the database. 
    * It uses a GameDbContext to interact with the database, adds sample game and player data, 
    * and saves the changes to the database.*/
    public static void Initialize(IServiceProvider serviceProvider)
    {
      using (var context = new GameDbContext(
          serviceProvider.GetRequiredService<DbContextOptions<GameDbContext>>()))
      {
        // Look for any games.
        if (context.Games.Any())
        {
          return;   // DB has been seeded
        }

        context.Games.AddRange(
            new Game
            {
              Name = "Chess",
              Genre = "Strategy",
              ReleaseDate = DateTime.Parse("1985-2-12")
            },

            new Game
            {
              Name = "Monopoly",
              Genre = "Board",
              ReleaseDate = DateTime.Parse("1933-3-22")
            }
        );

        context.Players.AddRange(
            new Player
            {
              Name = "Alice",
              Score = 1500
            },

            new Player
            {
              Name = "Bob",
              Score = 1250
            }
        );

        context.SaveChanges();
      }
    }
  }
}
