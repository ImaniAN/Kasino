using Kasino.Models;
using Kasino.Services;
using Microsoft.AspNetCore.Mvc;

namespace Kasino.Controllers
{  /*This code defines a PlayerController class in a C# ASP.NET Core Web API. 
    * It handles HTTP requests for player-related operations such as 
    * getting all players, getting a player by ID, and creating a new player. 
    * The controller interacts with a service (IPlayerService) to perform these operations asynchronously.*/

  [Route("api/[controller]")]
  [ApiController]
  public class PlayerController : ControllerBase
  {
    private readonly IPlayerService _playerService;

    public PlayerController(IPlayerService playerService)
    {
      _playerService = playerService;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<Player>>> GetPlayers()
    {
      return Ok(await _playerService.GetAllPlayersAsync());
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<Player>> GetPlayer(string id)
    {
      var player = await _playerService.GetPlayerByIdAsync(id);

      if (player == null)
      {
        return NotFound();
      }

      return Ok(player);
    }

    [HttpPost]
    public async Task<ActionResult<Player>> CreatePlayer(Player player)
    {
      await _playerService.CreatePlayerAsync(player);
      return CreatedAtAction(nameof(GetPlayer), new { id = player.Id }, player);
    }

    // Additional actions (e.g., Update, Delete) can be added here
  }
}