using Kasino.Models;

namespace Kasino.Repositories
{
  public interface IPlayerRepository
  {
    Task<IEnumerable<Player>> GetAllPlayersAsync();
    Task<Player> GetPlayerByIdAsync(string id);
    Task CreatePlayerAsync(Player player);
    // Additional methods for update, delete
  }
}
