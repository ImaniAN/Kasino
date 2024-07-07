namespace Kasino.Tests.Backend.DTOs
{
  using System;
  using System.Collections.Generic;
  using Kasino.Backend.DTOs;
  using Xunit;

  public class PlayersDtoTests
  {
    private PlayersDto _testClass;

    public PlayersDtoTests()
    {
      _testClass = new PlayersDto();
    }

    [Fact]
    public void CanSetAndGetPlayerId()
    {
      // Arrange
      var testValue = "TestValue2003054804";

      // Act
      _testClass.PlayerId = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.PlayerId);
    }

    [Fact]
    public void CanSetAndGetName()
    {
      // Arrange
      var testValue = "TestValue234350153";

      // Act
      _testClass.Name = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Name);
    }

    [Fact]
    public void CanSetAndGetScore()
    {
      // Arrange
      var testValue = 1505249572;

      // Act
      _testClass.Score = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Score);
    }

    [Fact]
    public void CanSetAndGetGames()
    {
      // Arrange
      var testValue = new List<GameDto>();

      // Act
      _testClass.Games = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Games);
    }
  }
}