using Microsoft.AspNetCore.SignalR;

namespace Kasino.Hubs
{
  public class GameHub : Hub
  {
    public async Task SendMessage(string user, string message)
    {
      await Clients.All.SendAsync("ReceiveMessage", user, message);
    }

    // Add additional real-time methods as needed for the game
  }
}