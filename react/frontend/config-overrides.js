const { override, disableChunk } = require('customize-cra');

module.exports = override(
  disableChunk()
);
