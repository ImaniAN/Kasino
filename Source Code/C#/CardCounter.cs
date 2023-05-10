public class CardCounter
{
	public CardCounter() {
		NumberOfCards = 0;
		NumberOfSpades = 0;
	}

	public void addCard(Card card)
	{
		if (card.suit == Card.Suit.SPADE)
			++NumberOfSpades;
		if (card.face == Card.Face.ACE)
			++nAces;
		if (card.face == (Card.Face) 2 && card.suit == Card.Suit.SPADE)
			hasLittleCasino = true;
		else if (card.face == (Card.Face) 10 && card.suit == Card.Suit.DIAMOND)
			hasBigCasino = true;
		++NumberOfCards;
	}

	public int getValue()
	{
		int rv = 0;
		if (hasBigCasino)
			rv += 2;
		if (hasLittleCasino)
			++rv;
		return rv;
	}

	public void addSweep()
	{
		++nSweeps;
	}

	public int NumberOfCards {get; private set;}
	public int NumberOfSpades {get; private set;}
	private int nAces = 0;
	int nSweeps = 0;
	bool hasBigCasino = false;
	bool hasLittleCasino = false;
}
