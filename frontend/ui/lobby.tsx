import * as React from 'react';
import WordsPicker from '~/ui/words_picker';
import OriginalWords from '~/words.json';

// TODO: remove jquery dependency
// https://stackoverflow.com/questions/47968529/how-do-i-use-jquery-and-jquery-ui-with-parcel-bundler
var jquery = require('jquery');
window.$ = window.jQuery = jquery;

export const Lobby = ({ defaultGameID }) => {
  const [newGameName, setNewGameName] = React.useState(defaultGameID);
  const [selectedLanguage, setSelectedLanguage] = React.useState('Words');
  const [words, setWords] = React.useState(OriginalWords);

  function handleNewGame(e) {
    e.preventDefault();
    if (!newGameName) {
      return;
    }

    $.post(
      '/next-game',
      JSON.stringify({
        language: selectedLanguage,
        game_id: newGameName,
        word_set: words[selectedLanguage].split(', '),
        create_new: false,
      }),
      g => {
        const newURL = (document.location.pathname = '/' + newGameName);
        window.location = newURL;
      }
    );
  }

  return (
    <div id="lobby">
      <p id="banner">
		A version of CODENAMES but with images and GIFS.
      </p>
      <div id="available-games">
        <form id="new-game">
          <p className="intro">
            Play Codememes online across multiple devices on a shared board. To
            create a new game or join an existing game, enter a game identifier choose a rating,
            and click 'GO'. 
          </p>
          <input
            type="text"
            id="game-name"
            autoFocus
            onChange={e => {
              setNewGameName(e.target.value);
            }}
            value={newGameName}
          />
          <button disabled={!newGameName.length} onClick={handleNewGame}>
            Go
          </button>

          <div id="new-game-options">
            {Object.keys(OriginalWords).map(_language => (
              <WordsPicker
                key={_language}
                words={words[_language]}
                onWordChange={e => {
                  setWords({ ...words, [_language]: e.target.value });
                }}
                language={_language}
                selectedLanguage={selectedLanguage}
                onSelectedLanguageChange={() => {
                  setSelectedLanguage(_language);
                }}
              />
            ))}
          </div>
        </form>
      </div>
    </div>
  );
};
