using Kasino.Models;

namespace Kasino.Repositories
{
  public interface IGameRepository
  {
    Task<IEnumerable<Game>> GetAllGamesAsync();
    Task<Game> GetGameByIdAsync(string id);
    Task CreateGameAsync(Game game);
    // Additional methods for update, delete
  }
}
