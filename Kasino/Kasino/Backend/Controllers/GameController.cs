using Microsoft.AspNetCore.Mvc;

namespace Kasino.Controllers
{
  [Route("api/[controller]")]
  [ApiController]
  public class GameController : ControllerBase
  {
    private readonly IGameService _gameService;

    public GameController(IGameService gameService)
    {
      _gameService = gameService;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<Game>>> GetGames()
    {
      return Ok(await _gameService.GetAllGamesAsync());
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<Game>> GetGame(string id)
    {
      var game = await _gameService.GetGameByIdAsync(id);

      if (game == null)
      {
        return NotFound();
      }

      return Ok(game);
    }

    [HttpPost]
    public async Task<ActionResult<Game>> CreateGame(Game game)
    {
      await _gameService.CreateGameAsync(game);
      return CreatedAtAction(nameof(GetGame), new { id = game.Id }, game);
    }

    // Additional actions (e.g., Update, Delete) can be added here
  }
}