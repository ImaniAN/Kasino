using AutoMapper;
using Kasino.Backend.DTOs;
using Kasino.Models;

namespace Kasino.Backend.Helpers
{
  public class MappingProfile : Profile
  {
    public MappingProfile()
    {
      // Define a mapping from the Player entity to the PlayerDTO
      CreateMap<Player, PlayerDTO>();

      // Define a mapping from the Game entity to the GameDTO
      CreateMap<Game, GameDTO>();
      // If you have other mappings, define them here as well
    }
  }
}