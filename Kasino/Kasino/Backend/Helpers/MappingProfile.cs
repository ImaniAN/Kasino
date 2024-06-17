using Kasino.Models;

namespace Kasino.Services
{
  public class MappingProfile : Profile
  {/*This code defines a MappingProfile class that inherits from Profile. 
    * It sets up mappings between Player and PlayerDto objects for conversion purposes.*/
    public MappingProfile()
    {
      CreateMap<Player, PlayerDto>(); // Map Player to PlayerDto
      CreateMap<PlayerDto, Player>(); // Map PlayerDto to Player
    }
  }
}