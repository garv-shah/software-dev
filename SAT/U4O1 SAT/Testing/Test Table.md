# Test Table

Created At: August 9, 2022 6:04 PM <br>
Created By: Garv <br>
Description: My Test Table for Maths Club <br>
Published: August 9, 2022 6:04 PM <br>
Tags: Programming, Software Development 3&4 <br>

| #   | Test Case                     | Reason                                                                                           | Test Data                                                                                                                                                            | Expected Res                                                                                                     | Actual Res                                                 | Actual Res (Media)                                                        | Pass / Fail? |
|-----|-------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|---------------------------------------------------------------------------|--------------|
| 1   | loginPage()                   | To see if the user can sign in or not                                                            | example@example.com  example1!                                                                                                                                       | The user logs in to the home page into the example account                                                       | The user logs in to the home page into the example account |                                                                           | Pass         |
| 2   | ForgotPasswordAction()        | To see if the user can reset their password on the login page                                    | gshah.6110@gmail.com                                                                                                                                                 | The user receives an email asking them to reset their password if they wish.                                     |                                                            | ![1](Test%20Table%20Media/Screen_Shot_2022-08-09_at_6.31.39_pm.png)       | Pass         |
| 3   | AppleProviderConfiguration()  | To see if the user can sign in with the Apple provider configuration                             | gshah.6110@gmail.com (Apple ID)                                                                                                                                      | The user uses Face ID to sign in without typing in a password                                                    |                                                            | ![2](Test%20Table%20Media/trim.1CBF1F30-E34B-4145-A3A1-746378A58C73.mov)  | Pass         |
| 4   | GoogleProviderConfiguration() | To see if the user can sign in with Google, without typing in their password                     | gshah.6110@gmail.com (Google Account)                                                                                                                                | The user is able to sign in using Google as a provider                                                           |                                                            | ![3](Test%20Table%20Media/trim.F3CA7F79-3CEC-41C4-BD23-87E241080DC8.mov)  | Pass         |
| 5   | register_page.dart            | See if the user can sign up without entering a username                                          | “”                                                                                                                                                                   | The app tells the user that a username is required                                                               |                                                            | ![4](Test%20Table%20Media/trim.EBFD51EB-8894-4DDA-9D68-6EADC829E798.mov)  | Fail         |
| 6   | register_page.dart            | See if the user can sign up with a username that is too long                                     | TestingVeryLongUsername                                                                                                                                              | The app tells the user that they cannot sign up with a username that is too long                                 |                                                            | ![5](Test%20Table%20Media/trim.6E25C03E-F7B8-4F1E-8DDD-F2A304B93D9B.mov)  | Fail         |
| 7   | register_page.dart            | See if the user can sign up without entering a username                                          | “”                                                                                                                                                                   | The app tells the user that a username is required                                                               |                                                            | ![6](Test%20Table%20Media/trim.C27F0CF8-97AB-47D0-AF64-875C63FF897C.mov)  | Pass         |
| 8   | register_page.dart            | See if the user can sign up with a username that is too long                                     | TestingVeryLongUsername                                                                                                                                              | The app tells the user that they cannot sign up with a username that is too long                                 |                                                            | ![7](Test%20Table%20Media/trim.3F1D717F-BDC6-4F4F-B40D-0387F397C480.mov)  | Pass         |
| 9   | register_page.dart            | See if the user can sign up with a valid username                                                | TestingVeryLongUsername                                                                                                                                              | The app creates the username for the user and navigates to the home page                                         |                                                            | ![8](Test%20Table%20Media/trim.EFCC2499-2718-494D-A511-3AE5216FB7E6.mov)  | Pass         |
| 10  | home_page.dart                | To make sure everything works as normal, and all sizing is correct for the usability of a user   | gshah.6110@gmail.com                                                                                                                                                 | Everything is sized as expected, and no information is cut off or not usable                                     |                                                            | ![9](Test%20Table%20Media/trim.354C02D9-C101-4E9E-81CA-2B5FE80522EA.mov)  | Pass         |
| 11  | leaderboards.dart             | To make sure all sizing is correct and there are no overflows to hinder usability                | gshah.6110@gmail.com                                                                                                                                                 | That everything is sized correctly and there are no overflows that would hinder usability                        |                                                            | ![10](Test%20Table%20Media/trim.5709DA4F-1FE0-4B17-B4A9-7B7F7FBF3D99.mov) | Fail         |
| 12  | leaderboards.dart             | To make sure all sizing is correct and there are no overflows to hinder usability                | gshah.6110@gmail.com                                                                                                                                                 | That everything is sized correctly and there are no overflows that would hinder usability                        |                                                            | ![11](Test%20Table%20Media/trim.A234A469-6046-4324-A7E2-2FE61D1DB0CB.mov) | Pass         |
| 13  | pfpUpdate()                   | To see if the user can update their profile picture and crop it                                  | Photo of Molly’s Cat                                                                                                                                                 | The user’s profile picture gets updated on the settings page locally first, then updated everywhere              |                                                            | ![12](Test%20Table%20Media/trim.11D0E386-F7E4-4D7C-8173-B310F5036688.mov) | Pass         |
| 14  | settings_page.dart            | To see if the user can update their username within the constraints of the app (username limits) | TestingVeryLongUsername                                                                                                                                              | The username should not be allowed to be entered                                                                 |                                                            | ![13](Test%20Table%20Media/trim.2CA8523F-B3C7-458A-BDD9-A4B1FC2F1641.mov) | Fail         |
| 15  | settings_page.dart            | To see if the user can update their username from the settings page                              | Bob                                                                                                                                                                  | The username should update                                                                                       |                                                            | ![14](Test%20Table%20Media/trim.52B1B73D-6B92-4F66-B311-FA881F7330F8.mov) | Fail         |
| 16  | settings_page.dart            | To see if the user can update their username from the settings page                              | Bob                                                                                                                                                                  | The username should update                                                                                       |                                                            | ![15](Test%20Table%20Media/trim.C5EDED9B-3E86-4118-822A-D0C806349A68.mov) | Pass         |
| 17  | settings_page.dart            | To see if the user can update their username within the constraints of the app (username limits) | TestingVeryLongUsername, Example                                                                                                                                     | The username should not be allowed to be entered                                                                 |                                                            | ![16](Test%20Table%20Media/trim.62BAF8E2-000E-4492-B6D8-AE1C20485722.mov) | Pass         |
| 18  | create_post_view.dart         | To see if the specified options can be serialised to JSON and edited again                       | Title: Test Post Description: Unit Testing Section: Drafts Create Quiz: True Start Date: 11/08/2022 End Date: 17/08/2022 Quiz Title: Quiz Quiz Description: Quizzing | The post should be created with the data supplied and be editable afterwards                                     |                                                            | ![17](Test%20Table%20Media/trim.DB34DE73-F924-4FFF-91EF-FC21B5C03EB6.mov) | Pass         |
| 19  | edit_question.dart            | To see if the information in each question can get saved and serialised locally                  | Test {num}                                                                                                                                                           | The questions and solutions should all be saved and editable while mov)ing around the post ui.                   |                                                            | ![18](Test%20Table%20Media/trim.0CBAB18E-72DC-42BF-BEDE-AA86A6CB17D9.mov) | Fail         |
| 20  | edit_question.dart            | To see if the information in each question can get saved and serialised locally                  | Test {num}                                                                                                                                                           | The questions and solutions should all be saved and editable while mov)ing around the post ui.                   |                                                            | ![19](Test%20Table%20Media/trim.8F3D3102-7AE4-4CC3-8B0F-6426169FC568.mov) | Pass         |
| 21  | post_view.dart                | To see if the post view works and renders without any usability issues                           | T3 W4                                                                                                                                                                | The post should load as expected from Firestore and not have any errors                                          |                                                            | ![20](Test%20Table%20Media/trim.3001119F-B153-4905-B00E-84B383D4387A.mov) | Pass         |
| 22  | quiz_view.dart                | To see if the quiz view works and renders without any usability issues                           | Addition                                                                                                                                                             | The quiz should load as expected from Firestore and not have any errors, and mark the answers correct at the end |                                                            | ![21](Test%20Table%20Media/trim.05F54170-B2DA-4F86-86A1-3814363DF7AE.mov) | Pass         |
| 23  | section_page                  | To see if searching works as intended with no usability issues                                   | Junior                                                                                                                                                               | It should be possible to search for posts by their in app contents and navigate to each quiz/post                |                                                            | ![22](Test%20Table%20Media/trim.B3B0141F-3D3B-437B-A0EC-B260436176BD.mov) | Pass         |

# Change Log

## Tests 5/6

These two tests failed because though they were not allowing the user to sign up as expected, they were not telling the
user why. Upon further investigation, it turns out that the following error was logged to the console:

```prolog
9.3.0 - [FirebaseFirestore][I-FST000001] Listen for query at userInfo failed: Missing or insufficient permissions.
[VERBOSE-2:ui_dart_state.cc(198)] Unhandled Exception: [cloud_firestore/permission-denied] The caller does not have permission to execute the specified operation.
#0      StandardMethodCodec.decodeEnvelope (package:flutter/src/services/message_codecs.dart:607:7)
#1      MethodChannel._invokeMethod (package:flutter/src/services/platform_channel.dart:167:18)
<asynchronous suspension>
#2      MethodChannel.invokeMapMethod (package:flutter/src/services/platform_channel.dart:367:43)
<asynchronous suspension>
#3      MethodChannelQuery.get (package:cloud_firestore_platform_interface/src/method_channel/method_channel_query.dart:96:42)
<asynchronous suspension>
#4      _JsonQuery.get (package:cloud_firestore/src/query.dart:390:9)
<asynchronous suspension>
#5      _RegisterPageState.build.<anonymous closure> (package:maths_club/screens/auth/register_page.dart:76:35)
<asynchronous suspension>
```

This error was caused by the security rules that were implemented, that blocked the user from reading other people’s
userInfo documents. This also showed that it actually wasn’t possible to register with the current code, so a change was
made to allow for the users to read each other’s documents (they don’t have sensitive data in them anyways, besides
maybe email)

### Redone: 7/8

## Test 11

This test failed because I did not consider the spacing in the double digits, and the last number subsequently overflows
because of this. The following is the error logged to the console:

```prolog
======== Exception caught by rendering library =====================================================
The following assertion was thrown during layout:
A RenderFlex overflowed by 4.0 pixels on the right.

The relevant error-causing widget was: 
  Row Row:file:///Users/garv/Documents/GitHub/maths_club/lib/screens/leaderboards.dart:40:16
The overflowing RenderFlex has an orientation of Axis.horizontal.
The edge of the RenderFlex that is overflowing has been marked in the rendering with a yellow and black striped pattern. This is usually caused by the contents being too big for the RenderFlex.

Consider applying a flex factor (e.g. using an Expanded widget) to force the children of the RenderFlex to fit within the available space instead of being sized to their natural size.
This is considered an error condition because it indicates that there is content that cannot be seen. If the content is legitimately bigger than the available space, consider clipping it with a ClipRect widget before putting it in the flex, or using a scrollable container rather than a Flex, like a ListView.
```

A change was made to make the area the points are in smaller, to allow for the position to take up more space. This will
allow it to go up to the thousands, while also leaving a lot of space for people to have high amounts of points.

### Redone: 12

## Tests 14/15

Test 14 failed because there was no validation happening with the username inside the settings page. This is a
combination of two issues, one more simple of a fix than the other. One is that the local settings textfield didn’t have
any validation, which is easier to fix, but the other is that the server side doesn’t have any validation, so new rules
are required.

The client-side code was actually surprisingly more difficult than expected, because the floating dialogue doesn’t have
any onSubmit() function, or a key for the validator, so I wasn’t able to add the username checking into the function
like I did it before, instead creating a popup.

The cloud function was updated to the following to enforce server side validation:

```tsx
let username = data.username;
if (username == null || username.isEmpty()) {
    throw new functions.https.HttpsError('invalid-argument', 'A username must be provided!');
} else if (context.auth?.uid == null) {
    throw new functions.https.HttpsError('unauthenticated', 'UID cannot be null');
} else if (username.length > 12) {
    throw new functions.https.HttpsError('permission-denied', 'The username cannot exceed 12 characters');
} else {
    let userInfoList = (await db.collection('userInfo').where("lowerUsername", '==', username.toLowerCase()).get()).docs;

    if (userInfoList.length != 0) {
        throw new functions.https.HttpsError('already-exists', 'UID cannot be null');
    }

    functions.logger.info(`Updating username for ${context.auth?.uid}`, {structuredData: true});

    // set displayName username
    await admin.auth().updateUser(context.auth!.uid, {
        displayName: username,
    })

    // set userInfo username
    await db.collection("userInfo").doc(context.auth!.uid).update({
        lowerUsername: username.toString().toLowerCase(),
        username: username,
    });

    // set quizPoints username
    await db.collection("quizPoints").doc(context.auth!.uid).update({
        username: username,
    });
}
```

This did not seem to quite work, throwing the following error with Test 15:

```prolog
[VERBOSE-2:ui_dart_state.cc(198)] Unhandled Exception: [firebase_functions/internal] INTERNAL

#0      StandardMethodCodec.decodeEnvelope (package:flutter/src/services/message_codecs.dart:607:7)
#1      MethodChannel._invokeMethod (package:flutter/src/services/platform_channel.dart:167:18)
<asynchronous suspension>
#2      MethodChannelHttpsCallable.call (package:cloud_functions_platform_interface/src/method_channel/method_channel_https_callable.dart:23:24)
<asynchronous suspension>
#3      HttpsCallable.call (package:cloud_functions/src/https_callable.dart:49:37)
<asynchronous suspension>
#4      _SettingsPageState.build.<anonymous closure>.<anonymous closure> (package:maths_club/screens/settings_page.dart:250:31)
<asynchronous suspension>

#0      StandardMethodCodec.decodeEnvelope (package:flutter/src/services/message_codecs.dart:607:7)
#1      MethodChannel._invokeMethod (package:flutter/src/services/platform_channel.dart:167:18)
<asynchronous suspension>
#2      MethodChannelHttpsCallable.call (package:cloud_functions_platform_interface/src/method_channel/method_channel_https_callable.dart:23:24)
<asynchronous suspension>
#3      HttpsCallable.call (package:cloud_functions/src/https_callable.dart:49:37)
<asynchronous suspension>
#4      _SettingsPageState.build.<anonymous closure>.<anonymous closure> (package:maths_club/screens/settings_page.dart:250:31)
<asynchronous suspension>
```

That’s not very helpful, but after checking the logs of the actual cloud function, it turns out that username.isEmpty is
not a function, so I just had to change that to `if (!username) {}` because apparently using if on a value in TypeScript
checks it for being empty or a null value, etc.

### Redone: 16/17

## Test 19

This test failed because no LATEX solution was provided. It tried to load in the LATEX data, but since none was
provided, it threw an error, as seen in the video. The error log was as follows (#10 - #125 have been omitted for
readability):

```prolog
======== Exception caught by widgets library =======================================================
The following RangeError was thrown building Builder:
RangeError (index): Invalid value: Valid value range is empty: 0

The relevant error-causing widget was: 
  MaterialApp MaterialApp:file:///Users/garv/Documents/GitHub/maths_club/lib/main.dart:41:38
When the exception was thrown, this was the stack: 
#0      List.[] (dart:core-patch/growable_array.dart:264:36)
#1      TeXParser.tokenize (package:math_keyboard/src/foundation/tex2math.dart:123:16)
#2      TeXParser.parse (package:math_keyboard/src/foundation/tex2math.dart:309:5)
#3      _EditQuestionState.initState (package:maths_club/screens/post_creation/edit_question.dart:44:51)
#4      StatefulElement._firstBuild (package:flutter/src/widgets/framework.dart:4942:57)
#5      ComponentElement.mount (package:flutter/src/widgets/framework.dart:4781:5)
...     Normal element mounting (4 frames)
#9      Element.inflateWidget (package:flutter/src/widgets/framework.dart:3817:16)
(elided 3 frames from dart:async)
====================================================================================================
```

The fix was relatively simple, and just involved changing a `widget.solution != null`
to `(widget.solution?.isNotEmpty ?? false)`, as the check before allowed the value through even if it equaled an empty
string, whereas the new one is more comprehensive.

### Redone: 20
