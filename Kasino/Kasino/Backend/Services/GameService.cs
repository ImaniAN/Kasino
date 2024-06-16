using Kasino.Models;
using Kasino.Repositories;

namespace Kasino.Services
{
  public class GameService : IGameService
  {
    private readonly IGameRepository _gameRepository;

    public GameService(IGameRepository gameRepository)
    {
      _gameRepository = gameRepository;
    }

    public async Task<IEnumerable<Game>> GetAllGamesAsync()
    {
      return await _gameRepository.GetAllGamesAsync();
    }

    public async Task<Game> GetGameByIdAsync(string id)
    {
      return await _gameRepository.GetGameByIdAsync(id);
    }

    public async Task CreateGameAsync(Game game)
    {
      await _gameRepository.CreateGameAsync(game);
    }

    // Additional methods for game logic
  }
}
