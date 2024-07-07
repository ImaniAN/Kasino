namespace Kasino.Tests.Services
{
  using System;
  using System.Collections.Generic;
  using System.Threading.Tasks;
  using Kasino.Models;
  using Kasino.Repositories;
  using Kasino.Services;
  using NSubstitute;
  using Xunit;

  public class PlayerServiceTests
  {
    private PlayerService _testClass;
    private IPlayerRepository _playerRepository;

    public PlayerServiceTests()
    {
      _playerRepository = Substitute.For<IPlayerRepository>();
      _testClass = new PlayerService(_playerRepository);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new PlayerService(_playerRepository);

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void CannotConstructWithNullPlayerRepository()
    {
      Assert.Throws<ArgumentNullException>(() => new PlayerService(default(IPlayerRepository)));
    }

    [Fact]
    public async Task CanCallGetAllPlayersAsync()
    {
      // Arrange
      _playerRepository.GetAllPlayersAsync().Returns(new[] { new Player("TestValue1968261400"), new Player("TestValue974450873"), new Player("TestValue1307971780") });

      // Act
      var result = await _testClass.GetAllPlayersAsync();

      // Assert
      await _playerRepository.Received().GetAllPlayersAsync();

      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CanCallGetPlayerByIdAsync()
    {
      // Arrange
      var id = "TestValue1585507303";

      _playerRepository.GetPlayerByIdAsync(Arg.Any<string>()).Returns(new Player("TestValue550248491"));

      // Act
      var result = await _testClass.GetPlayerByIdAsync(id);

      // Assert
      await _playerRepository.Received().GetPlayerByIdAsync(Arg.Any<string>());

      throw new NotImplementedException("Create or modify test");
    }

    [Theory]
    [InlineData(null)]
    [InlineData("")]
    [InlineData("   ")]
    public async Task CannotCallGetPlayerByIdAsyncWithInvalidId(string value)
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.GetPlayerByIdAsync(value));
    }

    [Fact]
    public async Task GetPlayerByIdAsyncPerformsMapping()
    {
      // Arrange
      var id = "TestValue1408275285";

      // Act
      var result = await _testClass.GetPlayerByIdAsync(id);

      // Assert
      Assert.Same(id, result.Id);
    }

    [Fact]
    public async Task CanCallUpdatePlayerScoreAsync()
    {
      // Arrange
      var id = "TestValue214449750";
      var newScore = 544510356;

      _playerRepository.GetPlayerByIdAsync(Arg.Any<string>()).Returns(new Player("TestValue833947108"));

      // Act
      var result = await _testClass.UpdatePlayerScoreAsync(id, newScore);

      // Assert
      await _playerRepository.Received().GetPlayerByIdAsync(Arg.Any<string>());
      await _playerRepository.Received().UpdatePlayerAsync(Arg.Any<Player>());

      throw new NotImplementedException("Create or modify test");
    }

    [Theory]
    [InlineData(null)]
    [InlineData("")]
    [InlineData("   ")]
    public async Task CannotCallUpdatePlayerScoreAsyncWithInvalidId(string value)
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.UpdatePlayerScoreAsync(value, 1236647969));
    }

    [Fact]
    public async Task CanCallDeletePlayerAsync()
    {
      // Arrange
      var id = "TestValue1348410770";

      _playerRepository.GetPlayerByIdAsync(Arg.Any<string>()).Returns(new Player("TestValue7898420"));

      // Act
      var result = await _testClass.DeletePlayerAsync(id);

      // Assert
      await _playerRepository.Received().GetPlayerByIdAsync(Arg.Any<string>());
      await _playerRepository.Received().DeletePlayerAsync(Arg.Any<Player>());

      throw new NotImplementedException("Create or modify test");
    }

    [Theory]
    [InlineData(null)]
    [InlineData("")]
    [InlineData("   ")]
    public async Task CannotCallDeletePlayerAsyncWithInvalidId(string value)
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.DeletePlayerAsync(value));
    }

    [Fact]
    public async Task CanCallCreatePlayerAsync()
    {
      // Arrange
      var player = new Player("TestValue1338046888");

      // Act
      var result = await _testClass.CreatePlayerAsync(player);

      // Assert
      await _playerRepository.Received().AddPlayerAsync(Arg.Any<Player>());

      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CannotCallCreatePlayerAsyncWithNullPlayer()
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.CreatePlayerAsync(default(Player)));
    }
  }
}