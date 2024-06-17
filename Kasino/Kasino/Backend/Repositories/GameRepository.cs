using Kasino.Data;
using Kasino.Models;

namespace Kasino.Repositories
{  /*This code snippet defines a GameRepository class that implements the IGameRepository interface. 
    * It contains methods for asynchronously retrieving all games, getting a game by its ID, and creating a new game. 
    * It also mentions the possibility of additional methods for updating and deleting games. 
    * The repository interacts with a GameDbContext to perform these operations.*/

  public class GameRepository : IGameRepository
  {
    private readonly GameDbContext _context;

    public GameRepository(GameDbContext context)
    {
      _context = context;
    }

    public async Task<IEnumerable<Game>> GetAllGamesAsync()
    {
      return await _context.Games.ToListAsync();
    }

    public async Task<Game> GetGameByIdAsync(string id)
    {
      return await _context.Games.FindAsync(id);
    }

    public async Task CreateGameAsync(Game game)
    {
      _context.Games.Add(game);
      await _context.SaveChangesAsync();
    }

    // Additional methods for update, delete
  }
}