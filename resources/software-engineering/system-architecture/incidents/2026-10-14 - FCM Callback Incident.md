# FCM Callback Incident

Date: 2026-10-14
Context: [[resources/software-engineering/system-architecture/2026-07-15 - FCM System Overview|FCM System Overview]]

## Background

eContract's callback was switched to the new integration flow ([[archives/next-actions/2026-10-12 - Deploy FCM to Production and Repoint the 230 Callback to Signgate|repointed to signgate]]).

## What Happened

Two contracts, `FIM-466` and `FIM-502`, were sent to eContract before the cutover. Their callbacks now run through the new flow, which no longer applies the old logic.

## Impact

The FIM side never received the signed results for those two contracts.

## Root Cause

The callback was switched, but records created under the old flow were not migrated. In-flight records kept the old shape while their callbacks followed the new path.

## Fix

FIM asked for the two signed contract files to rerun them by hand.

## Lesson

Before switching a callback, drain or migrate in-flight records — or keep the old path alive until they finish.
