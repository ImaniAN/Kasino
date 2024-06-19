using Kasino.Backend.Services;
using Kasino.Models;
using Kasino.Repositories;

namespace Kasino.Services
{
  /// <summary>
  /// Service for managing game data
  /// </summary>
  public class GameService : IGameService
  {
    private readonly IGameRepository _gameRepository;

    /// <summary>
    /// Constructor for GameService
    /// </summary>
    /// <param name="gameRepository">Game repository dependency</param>
    public GameService(IGameRepository gameRepository)
    {
      _gameRepository = gameRepository;
    }

    /// <summary>
    /// Get all games asynchronously
    /// </summary>
    /// <returns>The list of all games</returns>
    public async Task<IEnumerable<Game>> GetAllGamesAsync()
    {
      return await _gameRepository.GetAllGamesAsync();
    }

    /// <summary>
    /// Get a game by ID asynchronously
    /// </summary>
    /// <param name="id">Game ID</param>
    /// <returns>The game with the specified ID</returns>
    public async Task<Game> GetGameByIdAsync(string id)
    {
      return await _gameRepository.GetGameByIdAsync(id);
    }

    /// <summary>
    /// Create a new game asynchronously
    /// </summary>
    /// <param name="game">Game object to create</param>
    public async Task CreateGameAsync(Game game)
    {
      await _gameRepository.CreateGameAsync(game);
    }

    // Additional methods for game logic
  }
}