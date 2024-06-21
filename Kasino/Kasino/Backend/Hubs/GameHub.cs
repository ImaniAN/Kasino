using Microsoft.AspNetCore.SignalR;

/* This code defines a SignalR hub called GameHub that has a method SendMessage to send a
 * message to all clients connected to the hub using SignalR. The method SendMessage takes
 * a user and a message as parameters and broadcasts this message to all clients using the method SendAsync. */

namespace Kasino.Hubs
{
  public class GameHub : Hub
  {
    public async Task SendMessage(string user, string message)
    {
      await Clients.All.SendAsync("ReceiveMessage", user, message);
    }
  }
}