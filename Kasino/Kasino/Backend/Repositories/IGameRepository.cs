using Kasino.Models;

namespace Kasino.Repositories
{  /*This code snippet defines an interface IGameRepository with methods for asynchronously retrieving 
    * all games, getting a game by its ID, and creating a new game. 
    * It also mentions the possibility of additional methods for updating and deleting games.*/

  public interface IGameRepository
  {
    Task<IEnumerable<Game>> GetAllGamesAsync();

    Task<Game> GetGameByIdAsync(string id);

    Task CreateGameAsync(Game game);

    // Additional methods for update, delete
  }
}