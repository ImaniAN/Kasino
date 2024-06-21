using Kasino.Backend.Services;
using Kasino.Models;
using Microsoft.AspNetCore.Mvc;

namespace Kasino.Controllers
{
  [Route("api/[controller]")]
  [ApiController]
  public class GameController : ControllerBase
  {
    private readonly IGameService _gameService;

    /// <summary>
    /// Constructor for GameController class.
    /// </summary>
    /// <param name="gameService">The game service to be injected.</param>
    public GameController(IGameService gameService)
    {
      _gameService = gameService;
    }

    /// <summary>
    /// Retrieves all games asynchronously.
    /// </summary>
    [HttpGet(Name = "GetAllGames")]
    public async Task<ActionResult<IEnumerable<Game>>> GetGamesAsync()
    {
      return Ok(await _gameService.GetAllGamesAsync());
    }

    /// <summary>
    /// Retrieves a game by its ID asynchronously.
    /// </summary>
    /// <param name="id">The ID of the game to retrieve.</param>
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

    /// <summary>
    /// Creates a new game asynchronously.
    /// </summary>
    /// <param name="game">The game to create.</param>
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

    /// <summary>
    /// Returns a NotFound response with the specified game ID.
    /// </summary>
    /// <param name="id">The ID of the game not found.</param>
    private ActionResult NotFoundResponse(string id)
    {
      return NotFound($"Game with ID {id} not found.");
    }
  }
}