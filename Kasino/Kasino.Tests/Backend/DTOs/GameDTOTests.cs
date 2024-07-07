namespace Kasino.Tests.Backend.DTOs
{
  using System;
  using System.Collections.Generic;
  using Kasino.Backend.DTOs;
  using Xunit;

  public class GameSessionDtoTests
  {
    private GameSessionDto _testClass;

    public GameSessionDtoTests()
    {
      _testClass = new GameSessionDto();
    }

    [Fact]
    public void CanSetAndGetSessionId()
    {
      // Arrange
      var testValue = "TestValue2129682911";

      // Act
      _testClass.SessionId = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.SessionId);
    }

    [Fact]
    public void CanSetAndGetPlayers()
    {
      // Arrange
      var testValue = new List<PlayerDto>();

      // Act
      _testClass.Players = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Players);
    }

    [Fact]
    public void CanSetAndGetGameState()
    {
      // Arrange
      var testValue = "TestValue1602349680";

      // Act
      _testClass.GameState = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.GameState);
    }

    [Fact]
    public void CanSetAndGetScores()
    {
      // Arrange
      var testValue = new Dictionary<string, int>();

      // Act
      _testClass.Scores = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Scores);
    }

    [Fact]
    public void CanSetAndGetStartTime()
    {
      // Arrange
      var testValue = DateTime.UtcNow;

      // Act
      _testClass.StartTime = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.StartTime);
    }

    [Fact]
    public void CanSetAndGetEndTime()
    {
      // Arrange
      var testValue = DateTime.UtcNow;

      // Act
      _testClass.EndTime = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.EndTime);
    }
  }
}