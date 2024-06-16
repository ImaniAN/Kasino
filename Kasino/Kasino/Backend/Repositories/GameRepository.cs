using Kasino.Models;

namespace Kasino.Repositories
{
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
