namespace Kasino.Tests.Data
{
  using System;
  using System.Data.Entity;
  using Kasino.Data;
  using Kasino.Models;
  using Xunit;
  using T = System.String;

  public class GameDbContextTests
  {
    private GameDbContext _testClass;
    private DbContextOptions<GameDbContext> _options;

    public GameDbContextTests()
    {
      _options = new DbContextOptions<GameDbContext>();
      _testClass = new GameDbContext(_options);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new GameDbContext(_options);

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void CannotConstructWithNullOptions()
    {
      Assert.Throws<ArgumentNullException>(() => new GameDbContext(default(DbContextOptions<GameDbContext>)));
    }

    [Fact]
    public void CanSetAndGetCards()
    {
      // Arrange
      var testValue = new DbSet<Card>();

      // Act
      _testClass.Cards = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Cards);
    }

    [Fact]
    public void CanSetAndGetDecks()
    {
      // Arrange
      var testValue = new DbSet<Deck>();

      // Act
      _testClass.Decks = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Decks);
    }

    [Fact]
    public void CanSetAndGetGames()
    {
      // Arrange
      var testValue = new DbSet<Game>();

      // Act
      _testClass.Games = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Games);
    }

    [Fact]
    public void CanSetAndGetPlayers()
    {
      // Arrange
      var testValue = new DbSet<Player>();

      // Act
      _testClass.Players = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Players);
    }

    [Fact]
    public void CanSetAndGetMoves()
    {
      // Arrange
      var testValue = new DbSet<Move>();

      // Act
      _testClass.Moves = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Moves);
    }
  }

  public class DbContextOptions_1Tests
  {
    private DbContextOptions<T> _testClass;

    public DbContextOptions_1Tests()
    {
      _testClass = new DbContextOptions<T>();
    }
  }
}