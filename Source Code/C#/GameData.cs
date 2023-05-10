using System;
using System.Collections.Generic;

public class GameData {
	private GameData () {
		this.Table = new List<AbstractCard>();
	}

	public bool isTableEmpty () {
		return (Table.Count == 0);
	}

	public void trailCard (Card c) {
		Table.Add (new AbstractCard(c));
	}

	public List<AbstractCard> captureWithCard (Card c) {
		List<AbstractCard> rv = new List<AbstractCard>();
		foreach (AbstractCard card in Table) {
			if (card.Value == c.face)
				rv.Add(card);
		}

		if (rv.Count == 0)
			throw new Exception("No cards captured");
		rv.Add (new AbstractCard(c));
		return rv;
	}

	private Player GetPlayerWithMostSpades () {
		int nSpades = 0;
		Player maxPlayer = null;

		foreach (Player p in players) {
			// The most spades only counts if one player has more than all others.
			if (p.Counter.NumberOfSpades == nSpades) {
				maxPlayer = null;
				continue;
			}
			if (p.Counter.NumberOfSpades > nSpades) {
				nSpades = p.Counter.NumberOfSpades;
				maxPlayer = p;
			}
		}
		return maxPlayer;
	}

	private Player GetPlayerWithMostCards () {
		int nCards = 0;
		Player maxPlayer = null;

		foreach (Player p in players) {
			// The most cards only counts if one player has more than all others.
			if (p.Counter.NumberOfCards == nCards) {
				maxPlayer = null;
				continue;
			}
			if (p.Counter.NumberOfCards > nCards) {
				nCards = p.Counter.NumberOfCards;
				maxPlayer = p;
			}
		}
		return maxPlayer;
	}

	public int GetPlayerTentativeScore (Player player) {
		int rv = player.Counter.getValue();
		if (GetPlayerWithMostSpades () == player)
			++rv;
		if (GetPlayerWithMostCards () == player)
			rv += 3;
		return rv;
	}

	public List<AbstractCard> Table {get; private set;}
	protected List<Player> players;
	private List<Card> deck = DeckFactory.createDeck();
}
