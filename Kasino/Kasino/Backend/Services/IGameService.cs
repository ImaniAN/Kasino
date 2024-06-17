
using Kasino.Models;

namespace Kasino.Backend.Services
{/*This code snippet defines an interface IGameService with three asynchronous methods:

CreateGameAsync which takes a Game object and returns a Task.
GetAllGamesAsync which returns a Task of type object.
GetGameByIdAsync which takes a string id and returns a Task of type Game.*/
  public interface IGameService
  {
    Task CreateGameAsync(Game game);
    Task<object?> GetAllGamesAsync();
    Task<Game> GetGameByIdAsync(string id);

  }
}