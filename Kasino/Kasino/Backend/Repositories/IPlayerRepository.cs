using Kasino.Models;

namespace Kasino.Repositories
{  /*This code snippet defines an interface IPlayerRepository with methods for asynchronous operations on players:

GetAllPlayersAsync returns all players asynchronously.
GetPlayerByIdAsync fetches a player by id asynchronously.
CreatePlayerAsync adds a new player asynchronously.
UpdatePlayerAsync updates an existing player asynchronously.
DeletePlayerAsync removes a player asynchronously.*/

  public interface IPlayerRepository
  {
    Task<IEnumerable<Player>> GetAllPlayersAsync();
    Task<Player> GetPlayerByIdAsync(string id);
    Task CreatePlayerAsync(Player player);
    Task UpdatePlayerAsync(Player player);
    Task DeletePlayerAsync(Player player);
  }
}
