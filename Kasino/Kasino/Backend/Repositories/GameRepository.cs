using Kasino.Data;
using Kasino.Models;
using System.Data.Entity;

namespace Kasino.Repositories
{
  /// <summary>
  /// Repository for managing game data
  /// </summary>
  public class GameRepository : IGameRepository
  {
    private readonly GameDbContext _context;

    /// <summary>
    /// Constructor for GameRepository
    /// </summary>
    /// <param name="context">GameDbContext dependency</param>
    public GameRepository(GameDbContext context)
    {
      _context = context;
    }

    /// <summary>
    /// Get all games asynchronously
    /// </summary>
    /// <returns>The list of all games</returns>
    public async Task<IEnumerable<Game>> GetAllGamesAsync()
    {
      return await _context.Games.ToListAsync();
    }

    /// <summary>
    /// Get a game by ID asynchronously
    /// </summary>
    /// <param name="id">Game ID</param>
    /// <returns>The game with the specified ID</returns>
    public async Task<Game> GetGameByIdAsync(string id)
    {
      return await _context.Games.FindAsync(id);
    }

    /// <summary>
    /// Create a new game asynchronously
    /// </summary>
    /// <param name="game">Game object to create</param>
    public async Task CreateGameAsync(Game game)
    {
      _context.Games.Add(game);
      await _context.SaveChangesAsync();
    }

    // Additional methods for update, delete
  }
}