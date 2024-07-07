namespace Kasino.Tests.Backend.Models
{
  using System;
  using System.Collections.Generic;
  using Kasino.Backend.Models;
  using Kasino.Models;
  using Xunit;

  public class BuildTests
  {
    private Build _testClass;
    private List<Card> _cards;
    private Player _owner;

    public BuildTests()
    {
      _cards = new List<Card>();
      _owner = new Player("TestValue340114770");
      _testClass = new Build(_owner, _cards);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new Build(_cards);

      // Assert
      Assert.NotNull(instance);

      // Act
      instance = new Build(_owner, _cards);

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void CannotConstructWithNullCards()
    {
      Assert.Throws<ArgumentNullException>(() => new Build(default(List<Card>)));
      Assert.Throws<ArgumentNullException>(() => new Build(_owner, default(List<Card>)));
    }

    [Fact]
    public void CannotConstructWithNullOwner()
    {
      Assert.Throws<ArgumentNullException>(() => new Build(default(Player), _cards));
    }

    [Fact]
    public void OwnerIsInitializedCorrectly()
    {
      Assert.Same(_owner, _testClass.Owner);
    }

    [Fact]
    public void CanSetAndGetOwner()
    {
      // Arrange
      var testValue = new Player("TestValue802283007");

      // Act
      _testClass.Owner = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Owner);
    }

    [Fact]
    public void CardsIsInitializedCorrectly()
    {
      _testClass = new Build(_cards);
      Assert.Same(_cards, _testClass.Cards);
      _testClass = new Build(_owner, _cards);
      Assert.Same(_cards, _testClass.Cards);
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