namespace Kasino.Tests.Backend.Hubs
{
  using System;
  using System.Collections.Generic;
  using Kasino.Backend.Hubs;
  using Kasino.Models;
  using Xunit;

  public class GameStateTests
  {
    private GameState _testClass;

    public GameStateTests()
    {
      _testClass = new GameState();
    }

    [Fact]
    public void CanCallAddMove()
    {
      // Arrange
      var move = new Move(new Player("TestValue740471737"), new Card(1232697943, Suits.D, 1548308612), Move.MoveActionType.Capture);

      // Act
      _testClass.AddMove(move);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void CannotCallAddMoveWithNullMove()
    {
      Assert.Throws<ArgumentNullException>(() => _testClass.AddMove(default(Move)));
    }

    [Fact]
    public void CanCallCalculatePoints()
    {
      // Arrange
      var playerCards = new List<Card>();

      // Act
      var result = _testClass.CalculatePoints(playerCards);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void CannotCallCalculatePointsWithNullPlayerCards()
    {
      Assert.Throws<ArgumentNullException>(() => _testClass.CalculatePoints(default(List<Card>)));
    }
  }
}