const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth2').Strategy;

const GOOGLE_CLIENT_ID = '648161922905-cl8lnggdspfrvp37pl7gc88ebjggt75a.apps.googleusercontent.com';
const GOOGLE_CLIENT_SECRET = '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';

passport.use(
  new GoogleStrategy(
    {
      clientID: GOOGLE_CLIENT_ID,
      clientSecret: GOOGLE_CLIENT_SECRET,
      callbackURL: 'http://localhost:3000/auth/google/callback',
      // callbackURL: 'https://ajouiefinalproject.loca.lt/auth/google/callback',
      passReqToCallback: true,
    },
    function (request, accessToken, refreshToken, profile, done) {
      return done(null, profile);
    },
  ),
);

passport.serializeUser(function (user, done) {
  done(null, user);
});

passport.deserializeUser(function (user, done) {
  done(null, user);
});
