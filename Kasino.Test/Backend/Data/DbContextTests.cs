namespace Kasino.Tests.Data
{
  using System;
  using Kasino.Data;
  using Xunit;

  public class DbContextTests
  {
    private DbContext _testClass;
    private DbContextOptions<GameDbContext> _options;

    public DbContextTests()
    {
      _options = new DbContextOptions<GameDbContext>();
      _testClass = new DbContext(_options);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new DbContext(_options);

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void CannotConstructWithNullOptions()
    {
      Assert.Throws<ArgumentNullException>(() => new DbContext(default(DbContextOptions<GameDbContext>)));
    }
  }
}