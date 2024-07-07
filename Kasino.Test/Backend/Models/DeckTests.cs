namespace Kasino.Tests.Models
{
  using System;
  using System.Collections.Generic;
  using Kasino.Models;
  using Xunit;

  public class DeckTests
  {
    private Deck _testClass;

    public DeckTests()
    {
      _testClass = new Deck();
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new Deck();

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void CanCallShuffle()
    {
      // Act
      _testClass.Shuffle();

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void CanCallDishCard()
    {
      // Act
      var result = _testClass.DishCard();

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void CanSetAndGetCards()
    {
      // Arrange
      var testValue = new List<Card>();

      // Act
      _testClass.Cards = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Cards);
    }
  }
}