# Database Design

Created: June 15, 2022 10:17 AM
Tags: Design

As stated previously, my backend will be primarily powered by Firebase Firestore, which is a NoSQL database model that
organises data into documents, which are key-value pairs within themselves. Thanks to the way documents work, data will
be split up mostly based on permissions. For example, the global scope will have a collection of user documents named by
UUID, each storing data the individual user can both view and edit about themselves. This information will also be
publicly available for anyone else to view by their permission, including information such as username, email and/or
status. Information that should be able to be updated based on certain events but not directly editable by a user must
be handled by cloud functions not directly on the client device for security purposes. This would include figures such
as experience or level, as we do not want this to be directly editable by the user, but we still want it to be updated
based on contextual events. Finally, individual group information, private to a specified user will be stored in the
respective individual collection for said group.