using Kasino.Backend.Services;
using Kasino.Models;
using Microsoft.AspNetCore.Mvc;

namespace Kasino.Controllers
{  /*This code defines a GameController class that handles HTTP requests related to games. 
    * It uses attributes like [Route("api/[controller]")] and [ApiController] for routing and identifying it as a controller. 
    * The class has methods for getting all games, getting a game by ID, and creating a new game. 
    * It interacts with a service through dependency injection (IGameService) to perform these operations asynchronously.

*/

  [Route("api/[controller]")]
  [ApiController]
  public class GameController : ControllerBase
  {
    private readonly IGameService _gameService;

    public GameController(IGameService gameService)
    {
      _gameService = gameService;
    }

    [HttpGet(Name = "GetAllGames")]
    public async Task<ActionResult<IEnumerable<Game>>> GetGamesAsync()
    {
      return Ok(await _gameService.GetAllGamesAsync());
    }

    [HttpGet("{id}", Name = "GetGameById")]
    public async Task<ActionResult<Game>> GetGameAsync(string id)
    {
      var game = await _gameService.GetGameByIdAsync(id);
      if (game == null)
      {
        return NotFoundResponse(id);
      }
      else
      {
        return Ok(game);
      }
    }

    [HttpPost(Name = "CreateGame")]
    public async Task<ActionResult<Game>> CreateGameAsync(Game game)
    {
      if (!ModelState.IsValid)
      {
        return BadRequest(ModelState);
      }

      await _gameService.CreateGameAsync(game);
      return CreatedAtAction(nameof(GetGameAsync), new { id = game.Id }, game);
    }

    private ActionResult NotFoundResponse(string id)
    {
      return NotFound($"Game with ID {id} not found.");
    }
  }
}
